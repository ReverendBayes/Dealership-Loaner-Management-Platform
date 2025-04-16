// components/WalkaroundForm.tsx
import React, { useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useDropzone } from 'react-dropzone';

interface TireData {
  tread: string;
  psi: number;
  damage: string;
}

interface WalkaroundFormValues {
  tireFL: TireData;
  tireFR: TireData;
  tireRL: TireData;
  tireRR: TireData;
  notes: string;
  photos: File[];
}

const WalkaroundForm: React.FC = () => {
  const { register, control, handleSubmit } = useForm<WalkaroundFormValues>();
  const [uploadedImages, setUploadedImages] = useState<File[]>([]);

  const onDrop = (acceptedFiles: File[]) => {
    setUploadedImages((prev) => [...prev, ...acceptedFiles]);
  };

  const { getRootProps, getInputProps } = useDropzone({
    accept: { 'image/jpeg': [], 'image/png': [] },
    onDrop,
  });

  const onSubmit = (data: WalkaroundFormValues) => {
    console.log({ ...data, photos: uploadedImages });
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <h2 className="text-lg font-semibold text-gray-800">Walkaround Inspection</h2>

      {['FL', 'FR', 'RL', 'RR'].map((pos) => (
        <div key={pos} className="grid grid-cols-3 gap-4 border p-4 rounded-md">
          <label className="text-sm font-medium">Tire {pos} Tread</label>
          <select {...register(`tire${pos}.tread`)} className="form-select">
            <option value="6/32+">6/32+</option>
            <option value="2 to 4/32">2 to 4/32</option>
            <option value="2 or less">2 or less</option>
          </select>

          <label className="text-sm font-medium">PSI</label>
          <input type="number" {...register(`tire${pos}.psi`)} className="form-input" />

          <label className="text-sm font-medium">Damage</label>
          <select {...register(`tire${pos}.damage`)} className="form-select">
            <option value="none">None</option>
            <option value="cut">Cut</option>
            <option value="bulge">Bulge</option>
            <option value="flat">Flat</option>
          </select>
        </div>
      ))}

      <label className="block text-sm font-medium">Additional Notes</label>
      <textarea {...register("notes")} className="form-textarea w-full" rows={3} />

      <div {...getRootProps()} className="border-dashed border-2 p-6 text-center rounded-md bg-gray-50 hover:bg-gray-100">
        <input {...getInputProps()} />
        <p>Drag & drop vehicle photos here, or click to select.</p>
      </div>

      <div className="grid grid-cols-3 gap-4 mt-4">
        {uploadedImages.map((file, idx) => (
          <img
            key={idx}
            src={URL.createObjectURL(file)}
            alt={`upload-${idx}`}
            className="rounded shadow border"
          />
        ))}
      </div>

      <button type="submit" className="mt-6 bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">
        Submit Inspection
      </button>
    </form>
  );
};

export default WalkaroundForm;