from payheropy import initiate_payment

if __name__ == "__main__":
    response = initiate_payment("254712345678", 250)
    print(response)
