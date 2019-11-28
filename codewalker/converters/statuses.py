def convert(status: int):
    if status == 1:
        return "In Queue"
    elif status == 2:
        return "Processing"
    elif status == 3:
        return "Accepted"
    elif status == 4:
        return "Wrong Answer"
    elif status == 5:
        return "Time Limit Exceeded"
    elif status == 6:
        return "Compilation Error"
    elif status == 7:
        return "Runtime Error (SIGSEGV)"
    elif status == 8:
        return "Runtime Error (SIGXFSZ)"
    elif status == 9:
        return "Runtime Error (SIGFPE)"
    elif status == 10:
        return "Runtime Error (SIGABRT)"
    elif status == 11:
        return "Runtime Error (NZEC)"
    elif status == 12:
        return "Runtime Error (Other)"
    elif status == 13:
        return "Internal Error"
    elif status == 14:
        return "Exec Format Error"