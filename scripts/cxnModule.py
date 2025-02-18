
def get_cnx_info(entry):
    """Generate the construction information."""
    cnx_index = entry.get('cnx_index', '-')
    cnx_component = entry.get('cnx_component', '-')
    return f"{cnx_index}:{cnx_component}" if cnx_index != '-' and cnx_component != '-' else '-'