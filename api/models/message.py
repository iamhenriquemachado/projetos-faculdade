class Message:
    """
    A centralized repository for standardized API response messages.
    This prevents "magic strings" from being scattered throughout the codebase.
    """
    # --- Default Success Messages ---
    SUCCESS_DEFAULT = "Operation completed successfully."
    SUCCESS_CREATED = "The resource was created successfully."
    SUCCESS_UPDATED = "The resource was updated successfully."
    SUCCESS_DELETED = "The resource was deleted successfully."

    # --- Default Error Messages ---
    ERROR_DEFAULT = "An unexpected error occurred. Please try again later."
    ERROR_NOT_FOUND = "The requested resource could not be found."
    ERROR_INVALID_ID = "The provided ID is not valid."

    # --- Default Authentication Messages ---
    AUTH_LOGIN_SUCCESS = "You have been successfully logged in."
    AUTH_LOGIN_FAILED = "Invalid credentials."
    AUTH_LOGOUT_SUCCESS = "You have been successfully logged out."
    AUTH_REQUIRED = "Authentication is required to access this resource."
    AUTH_FORBIDDEN = "You do not have permission to perform this action."

    # --- Default Validation Messages ---
    VALIDATION_FAILED = "Validation failed. Check the fields."
    VALIDATION_REQUIRED = "The field is required."
    VALIDATION_INVALID_EMAIL = "Please enter a valid email address."
    VALIDATION_PASSWORD_SHORT = "Password must be at least 8 characters long."
    VALIDATION_PASSWORDS_NO_MATCH = "Passwords do not match."

   # --- Default Database Messages ---
    DATABASE_CONNECTED = "Database connection is OK."
    DATABASE_CONNECTION_FAILED = "Error: Could not connect to the database."
    DATABASE_QUERY_FAILED = "Error: The test query failed to return the expected result."

    # --- Default Transaction Messages ---
    TRANSACTION_USER_EXISTS = "The user does not exists in the database. Please check."
    TRANSACTION_INSUFICCIENT_BALANCE = "The user does not have enough balance in their account."

# To invoke the Message Class, use: `MSG.SUCCESS_CREATED`
MSG = Message()
