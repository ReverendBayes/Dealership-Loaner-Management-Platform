// pages/CheckIn.tsx
// Customer check-in: capture DL, insurance, walkaround, signature

import React, { useState } from 'react';
import UploadForm from '../components/UploadForm';
import WalkaroundForm from '../components/WalkaroundForm';
import SignaturePad from '../components/SignaturePad';

const CheckIn: React.FC = () => {
  const [insuranceFile, setInsuranceFile] = useState<File | null>(null);
  const [licenseFile, setLicenseFile] = useState<File | null>(null);
  const [signature, setSignature] = useState<string | null>(null);
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = () => {
    if (!insuranceFile || !licenseFile || !signature) return alert('Missing one or more required inputs.');
    // TODO: submit all data to backend
    setSubmitted(true);
  };

  if (submitted) {
    return <p className="text-center text-green-600 font-semibold mt-10">Check-in submitted successfully.</p>;
  }

  return (
    <div className="space-y-8 max-w-3xl mx-auto py-8">
      <h1 className="text-2xl font-semibold text-gray-800">Customer Check-In</h1>

      <UploadForm label="Upload Insurance Card" onFileAccepted={setInsuranceFile} />
      <UploadForm label="Upload Driver's License" onFileAccepted={setLicenseFile} />

      <WalkaroundForm />

      <SignaturePad onSave={setSignature} />

      <button
        onClick={handleSubmit}
        className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
      >
        Submit Check-In
      </button>
    </div>
  );
};

export default CheckIn;