from typing import List, Dict, Any
from .http_types import HttpRequest

BASE_URL = "https://community-api.xiaomawang.com/api/v1"

def _auth_headers(access_token: str) -> Dict[str, str]:
    if not isinstance(access_token, str) or not access_token.strip():
        raise ValueError("access_token required")
    return {"Access-Token": access_token}

def build_get_comment_list(access_token: str, page: int = 1, page_size: int = 10, report_status: int = 0) -> HttpRequest:
    url = f"{BASE_URL}/report/get-comment-list"
    params = {"page": page, "pageSize": page_size, "reportStatus": report_status}
    return HttpRequest(method="GET", url=url, params=params, headers=_auth_headers(access_token))

def build_get_report_info(access_token: str, report_id: int) -> HttpRequest:
    url = f"{BASE_URL}/report/get-info"
    params = {"reportId": report_id}
    return HttpRequest(method="GET", url=url, params=params, headers=_auth_headers(access_token))

def build_verify_comment(
    access_token: str,
    report_id: int,
    report_detail_ids: List[int],
    action: int,
    remark: str,
    reporter_message: str,
    user_message: str,
    reporter_is_send: int = 1,
    user_is_send: int = 1,
) -> HttpRequest:
    url = f"{BASE_URL}/report/verify-comment"
    data: Dict[str, Any] = {
        "reportId": report_id,
        "reporterIsSend": reporter_is_send,
        "userIsSend": user_is_send,
        "reportDetailIds": report_detail_ids,
        "action": action,
        "remark": remark,
        "reporterMessage": reporter_message,
        "userMessage": user_message,
    }
    return HttpRequest(method="POST", url=url, headers=_auth_headers(access_token), json=data) 