"""Lambda handler that validates and processes an order."""

from shared_utils import (
    log_event,
    requests_version,
    standard_response,
    validate_request,
)


def lambda_handler(event, context):
    log_event(
        "info",
        "Starting order processing",
        request_id=context.aws_request_id,
    )

    is_valid, error_message = validate_request(
        event,
        ["product_id", "quantity", "customer_id"],
    )

    if not is_valid:
        log_event(
            "error",
            "Order rejected because required data is missing",
            reason=error_message,
            request_id=context.aws_request_id,
        )
        return standard_response(400, {}, error_message)

    available_stock = 100
    quantity = event["quantity"]

    order = {
        "product_id": event["product_id"],
        "quantity": quantity,
        "customer_id": event["customer_id"],
        "available_stock": available_stock,
        "status": "approved" if available_stock >= quantity else "out_of_stock",
        "layer_dependency_version": requests_version(),
    }

    log_event(
        "info",
        "Order processed",
        status=order["status"],
        request_id=context.aws_request_id,
    )

    return standard_response(
        200,
        order,
        "Order processed successfully",
    )
