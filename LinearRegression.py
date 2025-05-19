def main():
    print("Hello from CI/CD Pipeline!")
    print("New change")

from sklearn.metrics import mean_squared_error

print("Sample MSE calculation:")
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
print("MSE:", mean_squared_error(y_true, y_pred))


if __name__ == "__main__":
    main()
