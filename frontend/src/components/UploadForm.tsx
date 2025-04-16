// components/UploadForm.tsx
import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';

interface UploadFormProps {
  onFileAccepted: (file: File) => void;
  label?: string;
}

const UploadForm: React.FC<UploadFormProps> = ({ onFileAccepted, label = "Upload Image" }) => {
  const [preview, setPreview] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const { getRootProps, getInputProps } = useDropzone({
    accept: { 'image/jpeg': [], 'image/png': [] },
    maxFiles: 1,
    onDrop: (acceptedFiles) => {
      const file = acceptedFiles[0];
      if (!file) return;
      setPreview(URL.createObjectURL(file));
      onFileAccepted(file);
      setError(null);
    },
    onDropRejected: () => {
      setError("Only JPG and PNG images are allowed.");
    },
  });

  return (
    <div className="bg-white shadow rounded-xl p-6 w-full">
      <label className="block text-sm font-medium text-gray-700 mb-2">{label}</label>

      <div
        {...getRootProps({
          className:
            'border-2 border-dashed border-gray-300 rounded-lg p-6 text-center cursor-pointer hover:border-blue-500 hover:bg-blue-50 transition',
        })}
      >
        <input {...getInputProps()} />
        <p className="text-sm text-gray-500">Click or drag a JPG or PNG to upload.</p>
      </div>

      {error && <p className="mt-2 text-sm text-red-500">{error}</p>}

      {preview && (
        <div className="mt-4">
          <img
            src={preview}
            alt="Preview"
            className="rounded-md border shadow max-h-48 mx-auto"
          />
        </div>
      )}
    </div>
  );
};

export default UploadForm;
