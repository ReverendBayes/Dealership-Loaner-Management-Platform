// components/ui/Button.tsx
// Reusable Axle-style primary and secondary buttons

import React from 'react';
import classNames from 'classnames';

type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: 'primary' | 'secondary';
};

const Button: React.FC<ButtonProps> = ({ variant = 'primary', className, children, ...props }) => {
  const baseStyles = 'px-4 py-2 rounded font-medium transition focus:outline-none';
  const variantStyles = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700',
    secondary: 'bg-white border border-gray-300 text-gray-700 hover:bg-gray-50',
  };

  return (
    <button
      className={classNames(baseStyles, variantStyles[variant], className)}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;