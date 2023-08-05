from datetime import datetime
from typing import Any, Dict

from yalexs.activity import (
    ACTION_BRIDGE_OFFLINE,
    ACTION_BRIDGE_ONLINE,
    ACTION_DOOR_CLOSED,
    ACTION_DOOR_OPEN,
    ACTION_DOORBELL_BUTTON_PUSHED,
    ACTION_DOORBELL_IMAGE_CAPTURE,
    ACTION_DOORBELL_MOTION_DETECTED,
    ACTION_LOCK_JAMMED,
    ACTION_LOCK_LOCK,
    ACTION_LOCK_LOCKING,
    ACTION_LOCK_UNLOCK,
    ACTION_LOCK_UNLOCKING,
    SOURCE_PUBNUB,
)
from yalexs.api_common import _activity_from_dict
from yalexs.doorbell import DOORBELL_STATUS_KEY, DoorbellDetail
from yalexs.lock import (
    DOOR_STATE_KEY,
    LOCK_STATUS_KEY,
    LockDetail,
    LockDoorStatus,
    LockStatus,
    determine_door_state,
    determine_lock_status,
)

from .api_common import _datetime_string_to_epoch
from .device import Device


def activities_from_pubnub_message(
    device: Device, date_time: datetime, message: Dict[str, Any]
):
    """Create activities from pubnub."""
    activities = []
    activity_dict = {
        "deviceID": device.device_id,
        "house": device.house_id,
        "deviceName": device.device_name,
    }
    info = message.get("info", {})
    context = info.get("context", {})
    accept_user = False
    if "startDate" in context:
        activity_dict["dateTime"] = _datetime_string_to_epoch(context["startDate"])
        accept_user = True
    elif "startTime" in info:
        activity_dict["dateTime"] = _datetime_string_to_epoch(info["startTime"])
        accept_user = True
    else:
        activity_dict["dateTime"] = date_time.timestamp() * 1000

    if isinstance(device, LockDetail):
        activity_dict["deviceType"] = "lock"
        activity_dict["info"] = info
        calling_user_id = message.get("callingUserID")
        # Only accept a UserID if we have a date/time
        # as otherwise it is a duplicate of the previous
        # activity
        if accept_user and calling_user_id:
            activity_dict["callingUser"] = {"UserID": calling_user_id}
        if "remoteEvent" in message:
            activity_dict["info"]["remote"] = True

        if LOCK_STATUS_KEY in message:
            status = message[LOCK_STATUS_KEY]
            if status == ACTION_BRIDGE_ONLINE:
                _add_activity(activities, activity_dict, ACTION_BRIDGE_ONLINE)
            elif status == ACTION_BRIDGE_OFFLINE:
                _add_activity(activities, activity_dict, ACTION_BRIDGE_OFFLINE)
            lock_status = determine_lock_status(status)
            if lock_status == LockStatus.LOCKED:
                _add_activity(activities, activity_dict, ACTION_LOCK_LOCK)
            elif lock_status == LockStatus.UNLOCKED:
                _add_activity(activities, activity_dict, ACTION_LOCK_UNLOCK)
            elif lock_status == LockStatus.LOCKING:
                _add_activity(activities, activity_dict, ACTION_LOCK_LOCKING)
            elif lock_status == LockStatus.UNLOCKING:
                _add_activity(activities, activity_dict, ACTION_LOCK_UNLOCKING)
            elif lock_status == LockStatus.JAMMED:
                _add_activity(activities, activity_dict, ACTION_LOCK_JAMMED)
        if DOOR_STATE_KEY in message:
            door_state = determine_door_state(message[DOOR_STATE_KEY])
            if door_state == LockDoorStatus.OPEN:
                _add_activity(activities, activity_dict, ACTION_DOOR_OPEN)
            elif door_state == LockDoorStatus.CLOSED:
                _add_activity(activities, activity_dict, ACTION_DOOR_CLOSED)

    elif isinstance(device, DoorbellDetail):
        activity_dict["deviceType"] = "doorbell"
        info = activity_dict["info"] = message.get("data", {})
        info.setdefault("image", info.get("result", {}))
        info.setdefault("started", activity_dict["dateTime"])
        info.setdefault("ended", activity_dict["dateTime"])

        if DOORBELL_STATUS_KEY in message:
            status = message[DOORBELL_STATUS_KEY]
            if status in (
                ACTION_DOORBELL_MOTION_DETECTED,
                ACTION_DOORBELL_IMAGE_CAPTURE,
                ACTION_DOORBELL_BUTTON_PUSHED,
            ):
                _add_activity(activities, activity_dict, status)

    return activities


def _add_activity(activities, activity_dict, action):
    activity_dict = activity_dict.copy()
    activity_dict["action"] = action
    activities.append(_activity_from_dict(SOURCE_PUBNUB, activity_dict))
