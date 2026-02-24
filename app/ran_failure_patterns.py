FAILURE_PATTERNS = {
    "rrc_setup_failure": r"rrc.*fail",
    "attach_failure": r"attach.*reject",
    "handover_failure": r"handover.*fail",
    "radio_link_failure": r"radio link failure|rlf",
    "ng_reset": r"ngap.*reset",
    "s1_reset": r"s1ap.*reset",
    "kernel_panic": r"kernel panic|fatal|memory corruption"
}