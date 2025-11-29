import streamlit as st
import math


st.title("Multi-Function Calculator")


st.sidebar.header("Calculator Options")
operation = st.sidebar.selectbox(
"Select Operation",
[
"Arithmetic ( + , - , * , / )",
"Modular",
"Exponential",
"Logarithmic",
]
)


# Input fields
a = st.number_input("Enter first number (a):", value=0.0)
b = st.number_input("Enter second number (b):", value=0.0)


st.write("### Result:")


# Arithmetic
if operation == "Arithmetic ( + , - , * , / )":
  op = st.selectbox("Select arithmetic operator", ["+", "-", "*", "/"])
if op == "+":
  st.success(f"a + b = {a + b}")
elif op == "-":
  st.success(f"a - b = {a - b}")
elif op == "*":
  st.success(f"a * b = {a * b}")
elif op == "/":
if b != 0:
  st.success(f"a / b = {a / b}")
else:
  st.error("Error: Division by zero is not allowed.")


# Modular
elif operation == "Modular":
if b != 0:
  st.success(f"a % b = {a % b}")
else:
  st.error("Error: Modulo by zero is not allowed.")


# Exponential
elif operation == "Exponential":
  st.success(f"a^b = {a ** b}")


# Logarithmic
elif operation == "Logarithmic":
  base = st.number_input("Log base (default e):", value=math.e)
if a > 0 and base > 0 and base != 1:
  st.success(f"log_base(a) = {math.log(a, base)}")
else:
  st.error("Error: Logarithm requires a > 0, base > 0, and base ≠ 1.")
