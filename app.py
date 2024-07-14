import streamlit as st

def calculate(num1, num2, operation):
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                st.error('Division by zero error', icon="🚨")
                return "Division by zero error"
            else:
                return num1 / num2
    except ValueError:
        return "Enter a valid numeric value"
    

def main():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")
    operation = st.selectbox("Select operation", ["+", "-", "*", "/"])

    result = calculate(num1, num2, operation)
    st.write(f"Result: {result}")


if __name__ == "__main__":
    main()