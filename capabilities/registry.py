from runtime.handlers import execute_handler


DEFAULT_POLICY = {
    "required": True,
    "stop_on_failure": True,
    "replayable": True,
    "retry_on_failure": False,
    "max_retries": 0,
    "failure_mode": "TERMINAL",
    "allow_degraded_continuation": False,
    "allow_skip_on_missing_dependencies": False,
    "requires_runtime_keys": [],
}


CAPABILITY_REGISTRY = {

    "route_analysis": {
        "handler": execute_handler,
        "description": "Initial request interpretation",
        "policy": {
            **DEFAULT_POLICY,
        },
    },

    "auth_validation": {
        "handler": execute_handler,
        "description": "Authentication validation probe",
        "policy": {
            **DEFAULT_POLICY,
            "retry_on_failure": True,
            "max_retries": 1,
            "failure_mode": "RECOVERABLE",
            "allow_degraded_continuation": True,
        },
    },

    "security_scan": {
        "handler": execute_handler,
        "description": "Security analysis execution",
        "policy": {
            **DEFAULT_POLICY,
            "requires_runtime_keys": [
                "response",
            ],
            "allow_skip_on_missing_dependencies": True,
        },
    },

    "reporting": {
        "handler": execute_handler,
        "description": "Runtime report generation",
        "policy": {
            **DEFAULT_POLICY,
            "replayable": False,
            "requires_runtime_keys": [
                "analysis",
            ],
            "allow_skip_on_missing_dependencies": True,
        },
    },
}
