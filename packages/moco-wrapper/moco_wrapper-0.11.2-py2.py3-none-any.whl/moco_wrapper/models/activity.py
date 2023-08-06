import datetime
from typing import List

from moco_wrapper.util.endpoint import Endpoint

from moco_wrapper.models.base import MWRAPBase
from moco_wrapper.models import objector_models as om

from enum import Enum


class ActivityRemoteService(str, Enum):
    """
    Enumeration for allowed values used that can be supplied for the ``remote_service`` argument in
    :meth:`.Activity.create` and :meth:`.Activity.update`

    .. code-block:: python

        from moco_wrapper import Moco
        from moco_wrapper.models.activity import ActivityRemoteService

        m = Moco()
        activity_create = m.Activity.create(
            ..
            remote_service = ActivityRemoteService.TRELLO
        )

    """
    TRELLO = "trello"
    JIRA = "jira"
    ASANA = "asana"
    BASECAMP = "basecamp"
    BASECAMP2 = "basecamp2"
    BASECAMP3 = "basecamp3"
    CLICKUP = "clickup"
    TOGGL = "toggl"
    MITE = "mite"
    GITHUB = "github"
    WUNDERLIST = "wunderlist"
    YOUTRACK = "youtrack"


class Activity(MWRAPBase):
    """
    Class for handling activities.

    Activities are always created for a project task. The order of things is `Project>Task>Activity`. An activity always
    belongs to a task and that task always belongs to a project.

    Example Usage:

    .. code-block:: python

        import datetime
        from moco_wrapper import Moco

        m = Moco()
        project_id = 2
        task_id = 3

        #log time
        created_activity = m.Activity.create(
            datetime.date(2020, 1, 1),
            project_id,
            task_id,
            0.25
            description="did things"
        )

    """

    @staticmethod
    def endpoints() -> List[Endpoint]:
        """
        Returns all endpoints associated with the model

        :returns: List of Endpoint objects
        :rtype: :class:`moco_wrapper.util.endpoint.Endpoint`

        """
        return [
            Endpoint("activity_get", "/activities/{id}", "GET", om.Activity),
            Endpoint("activity_getlist", "/activities", "GET", om.Activity),
            Endpoint("activity_create", "/activities", "POST", om.Activity),
            Endpoint("activity_update", "/activities/{id}", "PUT", om.Activity),
            Endpoint("activity_delete", "/activities/{id}", "DELETE", om.Activity),
            Endpoint("activity_start_timer", "/activities/{id}/start_timer", "PATCH", om.Activity),
            Endpoint("activity_stop_timer", "/activities/{id}/stop_timer", "PATCH", om.Activity),
            Endpoint("activity_disregard", "/activities/disregard", "POST")
        ]

    def __init__(self, moco):
        """
        Class constructor

        :param moco: An instance of :class:`moco_wrapper.Moco`
        """
        self._moco = moco

    def getlist(
        self,
        from_date: datetime.date,
        to_date: datetime.date,
        user_id: int = None,
        project_id: int = None,
        task_id: int = None,
        sort_by: str = None,
        sort_order: str = 'asc',
        page: int = 1,
    ):
        """
        Get a list of activities.

        :param from_date: Start date
        :param to_date: End date
        :param user_id: User Id the activity belongs to (default ``None``)
        :param project_id: Id of the project the activity belongs to (default ``None``)
        :param task_id: Id of the task the activity belongs to (default ``None``)
        :param sort_by: Field to sort results by (default ``None``)
        :param sort_order: asc or desc (default ``"asc"``)
        :param page: Page number (default 1)

        :type from_date: datetime.date, str
        :type to_date: datetime.date, str
        :type user_id: int
        :type project_id: int
        :type task_id: int
        :type sort_by: str
        :type sort_order: str
        :type page: int

        :returns: List of activities
        :rtype: :class:`moco_wrapper.util.response.PagedListResponse`
        """

        if task_id is not None and project_id is None:
            raise ValueError("If task_id is set, project id must also be set")

        params = {}

        if isinstance(from_date, datetime.date):
            params["from"] = self._convert_date_to_iso(from_date)
        else:
            params["from"] = from_date

        if isinstance(to_date, datetime.date):
            params["to"] = self._convert_date_to_iso(to_date)
        else:
            params["to"] = to_date

        for key, value in (
            ("user_id", user_id),
            ("project_id", project_id),
            ("task_id", task_id),
            ("page", page)
        ):
            if value is not None:
                params[key] = value

        if sort_by is not None:
            params["sort_by"] = "{} {}".format(sort_by, sort_order)

        return self._moco.get("activity_getlist", params=params)

    def get(
        self,
        activity_id: int
    ):
        """
        Get a single activity.

        :param activity_id: Id of the activity

        :type activity_id: int

        :returns: The activity object
        :rtype: :class:`moco_wrapper.util.response.ObjectResponse`
        """
        ep_params = {
            "id": activity_id
        }

        return self._moco.get("activity_get", ep_params=ep_params)

    def create(
        self,
        activity_date: datetime.date,
        project_id: int,
        task_id: int,
        hours: float = None,
        seconds: int = None,
        description: str = None,
        billable: bool = None,
        tag: str = None,
        remote_service: str = None,
        remote_id: int = None,
        remote_url: str = None
    ):
        """
        Create an activity.

        :param activity_date: Date of the activity
        :param project_id: Id of the project this activity belongs to
        :param task_id: Id of the task this activity belongs to
        :param hours: Hours to log to the activity (pass 0 to start a timer, if the date is today) (default ``None``)
        :param seconds: Pass seconds instead of hours to avoid rounding issues (default ``None``)
        :param description: Activity description text (default ``None``)
        :param billable: If this activity is billable
            (pass ``None`` if billing is dependent on project configuration) (default ``None``)
        :param tag: Tag string (default ``None``)
        :param remote_service: Name of the remote service referenced by the activity (default ``None``)
        :param remote_id: Id of the activity in the remote_service (default ``None``)
        :param remote_url: Url of the remote service (default ``None``)

        :type activity_date: datetime.date, str
        :type project_id: int
        :type task_id: int
        :type hours: float
        :type seconds: int
        :type description: str
        :type billable: bool
        :type tag: str
        :type remote_service: :class:`.ActivityRemoteService`, str
        :type remote_id: str
        :type remote_url: str

        :returns: The created activity
        :rtype: :class:`moco_wrapper.util.response.ObjectResponse`
        """

        if hours is None and seconds is None:
            raise ValueError("Pass either hours or seconds, both are missing")
        elif hours is not None and seconds is not None:
            raise ValueError("Pass either hours or seconds, not both")

        data = {
            "project_id": project_id,
            "task_id": task_id,
        }

        if isinstance(activity_date, datetime.date):
            data["date"] = self._convert_date_to_iso(activity_date)
        else:
            data["date"] = activity_date

        for key, value in (
            ("description", description),
            ("billable", billable),
            ("tag", tag),
            ("remote_service", remote_service),
            ("remote_id", remote_id),
            ("remote_url", remote_url),
            ("hours", hours),
            ("seconds", seconds)
        ):
            if value is not None:
                data[key] = value

        return self._moco.post("activity_create", data=data)

    def update(
        self,
        activity_id: int,
        activity_date: datetime.date = None,
        project_id: int = None,
        task_id: int = None,
        hours: float = None,
        seconds: int = None,
        description: str = None,
        billable: bool = None,
        tag: str = None,
        remote_service: str = None,
        remote_id: int = None,
        remote_url: str = None
    ):
        """
        Update an activity.

        :param activity_id: Id of the activity
        :param activity_date: Date of the activity (default ``None``)
        :param project_id: Id of the project this activity belongs to (default ``None``)
        :param task_id: Id of the task this activity belongs to (default ``None``)
        :param hours: Hours to log to the activity (pass 0 to start a timer, if the date is today) (default ``None``
        :param seconds: Pass seconds instead of hours to avoid rounding issues (default ``None``)
        :param description: Description text (default ``None``)
        :param billable: If this activity is billable
            (pass ``None``) if billing is dependent on project configuration) (default ``None``)
        :param tag: Tag string (default ``None``)
        :param remote_service: Name of the remote service referenced by the activity (default ``None``)
        :param remote_id: Id of the activity in the remote_service (default ``None``)
        :param remote_url: Url of the remote service (default ``None``)

        :type activity_id: int
        :type activity_date: datetime.date, str
        :type project_id: int
        :type task_id: int
        :type hours: float
        :type seconds: int
        :type description: str
        :type billable: bool
        :type tag: str
        :type remote_service: :class:`.ActivityRemoteService`, str
        :type remote_id: str
        :type remote_url: str

        :returns: The updated activity
        :rtype: :class:`moco_wrapper.util.response.ObjectResponse`
        """

        if hours is not None and seconds is not None:
            raise ValueError("Pass either seconds or hours, not both")

        ep_params = {
            "id": activity_id
        }

        data = {}
        for key, value in (
            ("date", activity_date),
            ("project_id", project_id),
            ("task_id", task_id),
            ("hours", hours),
            ("seconds", seconds),
            ("description", description),
            ("billable", billable),
            ("tag", tag),
            ("remote_service", remote_service),
            ("remote_id", remote_id),
            ("remote_url", remote_url)
        ):
            if value is not None:
                if key in ["date"] and isinstance(value, datetime.date):
                    data[key] = self._convert_date_to_iso(value)
                else:
                    data[key] = value

        return self._moco.put("activity_update", ep_params=ep_params, data=data)

    def start_timer(
        self,
        activity_id: int
    ):
        """
        Start a timer on the specified activity.

        Timers can only be started for activities of the current day.

        :param activity_id: Id of the activity

        :type activity_id: int

        :returns: The activity the timer was started for
        :rtype: :class:`moco_wrapper.util.response.ObjectResponse`

        .. note::

            Timers can only be started for activities of the current day
        """
        ep_params = {
            "id": activity_id
        }

        return self._moco.patch("activity_start_timer", ep_params=ep_params)

    def stop_timer(
        self,
        activity_id: int
    ):
        """
        Stop a timer on the specified activity.

        :param activity_id: Id of the activity

        :type activity_id: int

        :returns: The activity the timer was stopped for
        :rtype: :class:`moco_wrapper.util.response.ObjectResponse`
        """
        ep_params = {
            "id": activity_id
        }

        return self._moco.patch("activity_stop_timer", ep_params=ep_params)

    def delete(
        self,
        activity_id: int
    ):
        """
        Delete an activity.

        :param activity_id: Id of the activity to delete

        :type activity_id: int

        :returns: Empty response on success
        :rtype: :class:`moco_wrapper.util.response.EmptyResponse`
        """
        ep_params = {
            "id": activity_id
        }

        return self._moco.delete("activity_delete", ep_params=ep_params)

    def disregard(
        self,
        reason: str,
        activity_ids: list,
        company_id: int,
        project_id: int = None
    ):
        """
        Disregard activities.

        :param reason: Reason text for disregarding these activities
        :param activity_ids: List of activity ids to disregard
        :param company_id: Company id these activities belong to
        :param project_id: Project id these activities belong to (default ``None``)

        :type reason: str
        :type activity_ids: list
        :type company_id: int
        :type project_id: int

        :returns: List with the activity ids that were disregarded
        :rtype: :class:`moco_wrapper.util.response.PagedListResponse`
        """

        data = {
            "reason": reason,
            "activity_ids": activity_ids,
            "company_id": company_id,
        }

        for key, value in (
            ("project_id", project_id),
        ):
            if value is not None:
                data[key] = value

        return self._moco.post("activity_disregard", data=data)
