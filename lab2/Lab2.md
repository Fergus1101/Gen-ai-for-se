Requirements Specification

Step 1: Identify the formulation standard

The input is informal business and system information. It is not already written as a complete user story, use case, or formal specification. The requested formulation standard is User Story.

Step 2: Check whether another standard is more appropriate

The User Story standard is appropriate for the customer-visible capabilities because it expresses who needs a capability and why. However, the input also contains operational constraints and technical behavior, such as delivery radius, delivery time, route generation, payment methods, and future reuse. These details are better represented as separate acceptance criteria and supporting system requirements rather than one large user story.

Because the requested standard is User Story and remains suitable, the requirement is decomposed into several related user stories. No change of standard is required.

Step 3: Optimized user stories

US-1: Select a fulfilment method

As a customer,
I want to choose store pickup or delivery at checkout,
so that I can receive my order in the way that suits me.

Acceptance criteria:
- At checkout, the customer can select exactly one fulfilment method: pickup or delivery.
- For pickup, the existing in-store pickup process remains available.
- For delivery, the system requests and validates a delivery address before the order is placed.
- The selected fulfilment method is shown in the order confirmation.

US-2: Pay for a delivery order

As a customer ordering delivery,
I want to pay online by credit card, direct bank transfer, or PayPal,
so that I can complete my order without paying the rider.

Acceptance criteria:
- The customer can select credit card, direct bank transfer, or PayPal as the online payment method.
- The order is not confirmed as paid until the selected payment method reports success.
- A failed or cancelled payment does not create a confirmed delivery order.
- The customer receives confirmation of the selected payment method and payment status.

US-3: Check delivery availability

As a customer,
I want the system to tell me whether delivery is available for my address,
so that I know whether I can place a delivery order.

Acceptance criteria:
- The system accepts a delivery address during checkout.
- The system allows delivery only when the address is within the restaurant's defined 10-kilometre delivery radius.
- The system clearly informs the customer when the address is outside the delivery area.
- The system does not accept an outside-area address as a delivery order.

US-4: Receive a delivery-time commitment

As a customer ordering delivery,
I want to receive my order within 70 minutes of placing it,
so that I can plan when to expect my food and drinks.

Acceptance criteria:
- A delivery order records its placement time.
- The system calculates and displays a promised delivery time no later than 70 minutes after order placement.
- The customer can see the delivery status and promised time after placing the order.
- An order that cannot meet the 70-minute commitment is flagged for operational handling and the customer is informed.

US-5: Receive an automatically generated delivery route

As a delivery rider,
I want to receive an assigned route containing my delivery item list and turn-by-turn directions,
so that I can deliver each order efficiently.

Acceptance criteria:
- The system generates a route for an eligible delivery order.
- The assigned route includes the relevant delivery item list.
- The assigned route includes turn-by-turn directions provided through Google Maps.
- The route is available to the rider in the smartphone application.

US-6: Receive a route when becoming available

As a delivery rider,
I want to mark myself as available in the smartphone application,
so that the system can assign me a delivery route.

Acceptance criteria:
- A rider can mark themselves available in the smartphone application.
- The system assigns an eligible route to an available rider as soon as the rider becomes available.
- The system assigns routes only to riders who are available and operating within the configured delivery operation.
- The rider can view the assigned route and its item list in the application.

US-7: Configure the delivery service for reuse

As a restaurant operator,
I want the delivery service's restaurant-specific settings to be configurable,
so that the system can be reused by another restaurant without changing its core software.

Acceptance criteria:
- The delivery radius, delivery-time commitment, payment methods, fulfilment methods, and rider settings can be configured per restaurant.
- Restaurant-specific orders and delivery routes are kept separate from those of other restaurants.
- A new restaurant can configure its service without modifying the core delivery functionality.

Operational constraint:

The delivery operation must support 2 to 3 riders using e-bikes. This is a constraint on the operation and should not be treated as a user story unless a specific rider or operator capability is required.

Step 4: INVEST validation

The stories are valuable because each describes a clear customer, rider, or operator outcome. They are negotiable because the implementation details, such as the exact route-assignment algorithm, are not prescribed beyond the stated business needs. They are estimable and small because the original compound requirement has been divided into distinct capabilities. They are testable because each story has observable acceptance criteria.

The stories are sufficiently independent for analysis and prioritisation, although the delivery stories have implementation dependencies: delivery availability precedes delivery payment and fulfilment, and route assignment depends on a confirmed delivery order. These dependencies do not prevent the stories from being independently understood or tested.

Clarifications required before final baselining:

1. Is the 10-kilometre radius measured from one restaurant, from each restaurant, or from a configurable delivery location?
2. Does the 70-minute guarantee begin when the customer submits the order, when payment succeeds, or when the restaurant accepts the order?
3. What should happen when no rider is available or when all 2 to 3 e-bike riders are occupied?
4. Which payment provider and bank-transfer flow should be used, and what counts as successful payment for a bank transfer?
5. Is Google Maps a mandatory integration, and which Google Maps product and account will provide the directions?
6. For future reuse, should the system support multiple restaurants at the same time, or only be configurable for one restaurant deployment at a time?

Until these points are answered, the stories satisfy the INVEST criteria at a functional level, but the delivery-time, routing, payment, and reuse requirements cannot be considered fully unambiguous and ready for implementation.
