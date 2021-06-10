import sentry_sdk
import os
from sentry_sdk.integrations.flask import FlaskIntegration

# sentry_sdk.init(
#     "http://0097d94829f24c2dbbf5418dddc7378c@aom.apig.io:9000/4",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0,

# )
def sentry_init():
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        environment=os.getenv("SENTRY_ENVIRONMENT", "dev"),
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=os.getenv("SENTRY_TRACES_RATE", 1.0),
        integrations=[FlaskIntegration()],
    )
