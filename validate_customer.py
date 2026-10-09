"""Lambda handler that validates basic customer information."""

from shared_utils import (
    log_event,
    requests_version,
    standard_response,
    validate_request,
)


def lambda_handler(event, context):
    log_event(
        "info",
        "Starting customer validation",
        request_id=context.aws_request_id,
    )

    is_valid, error_message = validate_request(
        event,
        ["email", "name"],
    )

    if not is_valid:
        log_event(
            "error",
            "Customer rejected because required data is missing",
            reason=error_message,
            request_id=context.aws_request_id,
        )
        return standard_response(400, {}, error_message)

    customer = {
        "email": event["email"],
        "name": event["name"],
        "status": "active",
        "profile": "standard",
        "layer_dependency_version": requests_version(),
    }

    log_event(
        "info",
        "Customer validated",
        email=event["email"],
        request_id=context.aws_request_id,
    )

    return standard_response(
        200,
        customer,
        "Customer validated successfully",
    )
