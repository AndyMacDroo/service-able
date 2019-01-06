class ServiceableService:

    service_name = None
    check_me = None
    available_at = None
    expect = None
    log = None

    is_healthy = False

    def __init__(self, name):
        self.service_name = name

    def set_is_healthy(self, is_healthy):
        self.is_healthy = is_healthy
        return self

    def set_check_me(self, check_me):
        self.check_me = check_me
        return self

    def set_available_at(self, available_at):
        self.available_at = available_at
        return self

    def set_expect(self, expect):
        self.expect = expect
        return self

    def set_log(self, log):
        self.log = log
        return self

    def __eq__(self, other):
        return self.service_name == other.service_name \
               and self.log == other.log \
               and self.check_me == other.check_me \
               and self.expect == other.expect \
               and self.available_at == other.available_at

    def __repr__(self):
        return "%s" % (self.service_name)