

class ServiceableConfig:

    serviceable_modes = ["daemon", "one-shot"]
    active_mode = None

    def __init__(self):
        self.active_mode = self.serviceable_modes[0]
        pass

    def set_active_mode(self, active_mode):
        if active_mode in self.serviceable_modes:
            self.active_mode = active_mode
        else:
            raise ValueError("Invalid mode specified")
        return self