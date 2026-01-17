# Sale Advance Payment Method Selection

## Overview

This module extends the `sale_advance_payment` module to add payment method selection functionality to the advance payment wizard.

## Features

1. **Journal Configuration**
   - Adds a `show_in_advance_payment` checkbox to payment method lines in journal configuration
   - Available in both Incoming and Outgoing payment tabs
   - Controls which payment methods appear in the advance payment wizard

2. **Enhanced Advance Payment Wizard**
   - Changes "Payment Method" label to "Journal" for clarity
   - Adds new "Payment Method" field for selecting specific payment method lines
   - Dynamic filtering based on:
     - Selected journal
     - Payment type (inbound/outbound)
     - Payment methods marked as "Show in Advance Payment"

3. **Automatic Domain Updates**
   - Payment method field automatically updates when journal or payment type changes
   - Only shows relevant payment methods based on current selection

## Configuration

1. Go to Accounting → Configuration → Journals
2. Select a journal (Bank or Cash)
3. In the Incoming/Outgoing Payments tabs, check "Show in Advance Payment" for the payment methods you want to make available in the wizard

## Usage

1. Open a Sale Order
2. Click "Advance Payment" button
3. Select a Journal
4. Select Payment Type (Inbound/Outbound)
5. Choose from filtered Payment Methods
6. Complete the payment

## Technical Details

- **Odoo Version**: 18.0
- **Dependencies**: sale_advance_payment
- **License**: AGPL-3

## Author

Samad Alimadadi
