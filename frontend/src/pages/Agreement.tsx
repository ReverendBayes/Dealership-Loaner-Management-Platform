// pages/Agreement.tsx
// Displays signed agreement PDF + signature preview

import React, { useState } from 'react';
import AgreementReview from '../components/AgreementReview';

const AgreementPage: React.FC = () => {
  const [submitted, setSubmitted] = useState(false);

  if (submitted) {
    return <p className="text-center text-green-600 font-semibold mt-10">Agreement confirmed and saved.</p>;
  }

  return (
    <div className="py-10">
      <AgreementReview
        customerName="Megan Harper"
        vehicle="2024 BMW 330i (P7N04476)"
        agreementUrl="/sample/agreement_MeganHarper.pdf"
        signatureUrl="/sample/signature_MeganHarper.png"
        onConfirm={() => setSubmitted(true)}
      />
    </div>
  );
};

export default AgreementPage;