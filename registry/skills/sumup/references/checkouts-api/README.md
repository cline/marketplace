# Checkouts API (Online)

> Prefer the latest SumUp docs first: `https://developer.sumup.com/online-payments/index.md`
> LLM entrypoint for discovery: `https://developer.sumup.com/llms.txt`

## Create checkout (server-to-server)

```bash
curl -X POST https://api.sumup.com/v0.1/checkouts \
  -H "Authorization: Bearer $SUMUP_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "merchant_code": "ME7RMQN3",
    "amount": 15.0,
    "currency": "EUR",
    "checkout_reference": "unique-checkout-ref-123"
  }'
```

## Use checkout ID in secure online flows

- Prefer `references/checkout-widget/README.md` for embedded payment UI.
- Use `references/webhooks-3ds/README.md` for async confirmation and 3DS handling patterns.

## Reading Order

1. This file.
2. `references/online-testing/README.md` for sandbox test cards and failure scenarios.
3. `references/checkout-widget/README.md` if using hosted or embedded checkout UI.
4. `references/webhooks-3ds/README.md` to finalize async lifecycle handling.

## See Also

- `references/online-testing/README.md`
- `references/checkout-widget/README.md`
- `references/webhooks-3ds/README.md`
- `references/apm/README.md`
- `references/nodejs/README.md`
- `references/go/README.md`
- `references/python/README.md`
- `references/java/README.md`
- `references/php/README.md`
- `references/rust/README.md`
- `references/dotnet/README.md`
