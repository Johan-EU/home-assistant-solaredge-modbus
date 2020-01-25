DOMAIN = "solaredge_modbus"

SENSOR_TYPES = {
    "AC_Current": ["AC Current", "accurrent", "A", "mdi:current-ac", None],
    "AC_CurrentA": ["AC Current A", "accurrenta", "A", "mdi:current-ac", None],
    "AC_CurrentB": ["AC Current B", "accurrentb", "A", "mdi:current-ac", None],
    "AC_CurrentC": ["AC Current C", "accurrentc", "A", "mdi:current-ac", None],
    "AC_VoltageAB": ["AC Voltage AB", "acvoltageab", "V", None, None],
    "AC_VoltageBC": ["AC Voltage BC", "acvoltagebc", "V", None, None],
    "AC_VoltageCA": ["AC Voltage CA", "acvoltageca", "V", None, None],
    "AC_VoltageAN": ["AC Voltage AN", "acvoltagean", "V", None, None],
    "AC_VoltageBN": ["AC Voltage BN", "acvoltagebn", "V", None, None],
    "AC_VoltageCN": ["AC Voltage CN", "acvoltagecn", "V", None, None],
    "AC_Power": ["AC Power", "acpower", "W", "mdi:solar-power", None],
    "AC_Frequency": ["AC Frequency", "acfreq", "Hz", None, None],
    "AC_VA": ["AC VA", "acva", "VA", None, None],
    "AC_VAR": ["AC VAR", "acvar", "VAR", None, None],
    "AC_PF": ["AC PF", "acpf", "%", None, None],
    "AC_Energy_KWH": ["AC Energy KWH", "acenergy", "kWh", "mdi:solar-power", None],
    "DC_Current": ["DC Current", "dccurrent", "A", "mdi:current-dc", None],
    "DC_Voltage": ["DC Voltage", "dcvoltage", "V", None, None],
    "DC_Power": ["DC Power", "dcpower", "W", "mdi:solar-power", None],
    "Temp_Sink": ["Temp Sink", "tempsink", "°C", None, None],
    "Status": ["Status", "status", None, None, None],
    "Status_Vendor": ["Status Vendor", "statusvendor", None, None, None]
}