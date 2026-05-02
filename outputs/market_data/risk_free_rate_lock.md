# Risk-Free Rate Lock

## Purpose

This file locks the draft risk-free rate assumption used in the SSRN verification layer.

## Locked Draft Rate

```text
India 10-year government bond yield: 7.01%
Date reference: May 1, 2026 close / used for May 2, 2026 market-data review
Status: Draft locked for sensitivity review, final source citation still required in manuscript references
```

## Source Note

The rate was selected because the market-data artifact timestamp is `2026-05-02 01:31 UTC`, and contemporary market reporting stated that India's 10-year benchmark government bond yield closed at 7.01% on Thursday after breaching the 7% mark.

## Model Treatment

The rate is used as the working risk-free rate in the normalized beta/WACC review table.

## Final SSRN Caution

Before final SSRN upload, the paper should cite the exact source used for the 10-year G-sec yield and confirm whether the final market-data date remains May 2, 2026. If the market data are refreshed again, this file should be refreshed as well.

## Research Boundary

This file is for research documentation only. It is not investment advice or financial advice.
