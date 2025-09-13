# email_filter.py
def filter_emails(emails, keyword="khẩn cấp"):
    """
    Trả về danh sách email có chứa từ khóa.
    """
    important = [e for e in emails if keyword.lower() in e.lower()]
    return important
