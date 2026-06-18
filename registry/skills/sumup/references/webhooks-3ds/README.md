# Webhooks and 3DS

> Prefer the latest SumUp docs first: `https://developer.sumup.com/online-payments/webhooks/index.md`
> LLM entrypoint for discovery: `https://developer.sumup.com/llms.txt`

## 3DS flow

1. Include `redirect_url` on checkout creation.
2. Process checkout and inspect `next_step`.
3. Redirect/post customer to `next_step.url` with full `next_step.payload`.
4. After challenge, verify status using retrieve-checkout API.

## Webhooks

- Subscribe by setting `return_url` at checkout creation.
- Expect checkout status change events.
- Respond quickly with empty `2xx`.
- Treat webhook as signal; re-fetch and verify checkout state from API.
- Implement idempotent processing for retries.

## Reading Order

1. This file.
2. `references/checkouts-api/README.md` for checkout lifecycle API calls.
3. `references/checkout-widget/README.md` for frontend callback integration.

## See Also

- `references/online-testing/README.md`
- `references/checkouts-api/README.md`
- `references/checkout-widget/README.md`
- `references/react-native-sdk/README.md`
- `references/swift-checkout-sdk/README.md`
