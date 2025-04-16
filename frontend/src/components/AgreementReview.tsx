// components/AgreementReview.tsx
// Component styled to match Axle's UI: clean white layout, blue accents, readable typography
// Pseudocode:
// - Display customer name, vehicle
// - Link to generated PDF
// - Show saved signature image
// - Confirm button triggers submission handler

import React from 'react';

interface AgreementReviewProps {
  customerName: string;
  vehicle: string;
  agreementUrl: string;
  signatureUrl: string;
  onConfirm: () => void;
}

const AgreementReview: React.FC<AgreementReviewProps> = ({
  customerName,
  vehicle,
  agreementUrl,
  signatureUrl,
  onConfirm,
}) => {
  return (
    <div className="max-w-2xl mx-auto bg-white rounded-lg shadow p-6 space-y-6">
      <h2 className="text-xl font-semibold text-gray-800">Review Agreement</h2>

      <div>
        <p className="text-sm text-gray-600">Customer:</p>
        <p className="text-md font-medium">{customerName}</p>
      </div>

      <div>
        <p className="text-sm text-gray-600">Vehicle:</p>
        <p className="text-md font-medium">{vehicle}</p>
      </div>

      <div>
        <p className="text-sm text-gray-600">Agreement PDF:</p>
        <a href={agreementUrl} target="_blank" rel="noopener noreferrer" className="text-blue-600 underline">
          View Agreement
        </a>
      </div>

      <div>
        <p className="text-sm text-gray-600">Signature:</p>
        <img src={signatureUrl} alt="Signature" className="border rounded shadow w-full max-w-xs" />
      </div>

      <button
        onClick={onConfirm}
        className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
      >
        Confirm and Submit
      </button>
    </div>
  );
};

export default AgreementReview;