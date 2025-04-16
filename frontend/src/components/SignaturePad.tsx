// components/SignaturePad.tsx
import React, { useRef } from 'react';
import SignatureCanvas from 'react-signature-canvas';

interface SignaturePadProps {
  onSave: (dataURL: string) => void;
}

const SignaturePad: React.FC<SignaturePadProps> = ({ onSave }) => {
  const sigRef = useRef<SignatureCanvas>(null);

  const handleClear = () => sigRef.current?.clear();
  const handleSave = () => {
    const data = sigRef.current?.getTrimmedCanvas().toDataURL('image/png');
    if (data) onSave(data);
  };

  return (
    <div className="w-full max-w-md mx-auto">
      <label className="block text-sm font-medium text-gray-700 mb-1">Signature</label>
      <div className="border rounded bg-white shadow">
        <SignatureCanvas
          ref={sigRef}
          penColor="black"
          canvasProps={{ width: 400, height: 200, className: 'w-full h-auto' }}
        />
      </div>
      <div className="flex justify-between mt-2">
        <button type="button" onClick={handleClear} className="text-sm text-gray-500 hover:text-red-600">Clear</button>
        <button type="button" onClick={handleSave} className="text-sm text-blue-600 hover:underline">Save</button>
      </div>
    </div>
  );
};

export default SignaturePad;