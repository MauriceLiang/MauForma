import type { ComponentPropsWithoutRef, ReactNode } from "react";

type Variant = "primary" | "secondary" | "ghost" | "danger";
type Size = "sm" | "md";
export type UiButtonProps = Omit<ComponentPropsWithoutRef<"button">, "children"> & {
  variant?: Variant;
  size?: Size;
  loading?: boolean;
  children: ReactNode;
};

export function UiButton({
  variant = "primary", size = "md", loading = false, disabled = false,
  type = "button", className = "", children, ...rest
}: UiButtonProps) {
  return (
    <button
      {...rest}
      type={type}
      className={`sp-button sp-button--${variant} sp-button--${size} ${className}`.trim()}
      disabled={disabled || loading}
      aria-busy={loading || undefined}
    >
      {loading && <span className="sp-button__spinner" aria-hidden="true" />}
      {children}
    </button>
  );
}
