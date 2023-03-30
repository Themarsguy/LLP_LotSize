while True:
    risk_tolerance = float(input("Enter the risk tolerance amount: $"))
    stop_loss = int(input("Enter the stop loss in pips: "))

    loss_per_pip = round(risk_tolerance / stop_loss, 2)
    print(f"The loss per pip is: {loss_per_pip}")

    if loss_per_pip > 0.01:
        standard_lots = int(loss_per_pip // 10)
        remaining_loss = loss_per_pip - standard_lots * 10

        mini_lots = int(remaining_loss // 1)
        remaining_loss -= mini_lots * 1

        micro_lots = int(remaining_loss // 0.1)

        print("Recommended lot size:")
        print(f"Standard lots: {standard_lots}")
        print(f"Mini lots: {mini_lots}")
        print(f"Micro lots: {micro_lots}")

    elif loss_per_pip <= 0.01:
        micro_lots = int(loss_per_pip // 0.01)

        print("Recommended lot size:")
        print(f"Standard lots: 0")
        print(f"Mini lots: 0")
        print(f"Micro lots: {micro_lots}")

    else:
        print("Error: Invalid input.")

    choice = input("Do you want to calculate again? (Y/N): ")
    if choice.lower() != "y":
        break
