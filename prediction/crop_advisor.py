
def explain_crop_conditions(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    """
    Explain the soil and climate conditions provided by the user.
    This first version is rule-based, not a trained AI model.
    """

    results = []

    if nitrogen < 50:
        results.append("Nitrogen level is relatively low.")
    elif nitrogen > 150:
        results.append("Nitrogen level is relatively high.")
    else:
        results.append("Nitrogen level is in the middle range.")

    if phosphorus < 30:
        results.append("Phosphorus level is relatively low.")
    else:
        results.append("Phosphorus level is not low.")

    if potassium < 30:
        results.append("Potassium level is relatively low.")
    else:
        results.append("Potassium level is not low.")

    if temperature < 15:
        results.append("The temperature is relatively cool.")
    elif temperature > 30:
        results.append("The temperature is relatively hot.")
    else:
        results.append("The temperature is moderate.")

    if humidity < 40:
        results.append("Humidity is relatively low.")
    else:
        results.append("Humidity is not low.")

    if ph < 5.5:
        results.append("The soil is acidic.")
    elif ph > 7.5:
        results.append("The soil is alkaline.")
    else:
        results.append("The soil pH is in a broadly common range.")

    if rainfall < 50:
        results.append("Rainfall is low.")
    else:
        results.append("Rainfall is not low.")

    return results
