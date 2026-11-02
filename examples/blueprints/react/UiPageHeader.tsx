import type { ReactNode } from "react";

export type UiPageHeaderProps = {
  title: string;
  description?: string;
  density?: "compact" | "comfortable";
  actions?: ReactNode;
};

export function UiPageHeader({ title, description, density = "compact", actions }: UiPageHeaderProps) {
  return (
    <header className={`sp-page-header sp-page-header--${density}`}>
      <div className="sp-page-header__copy">
        <h1 className="sp-page-header__title">{title}</h1>
        {description && <p className="sp-page-header__description">{description}</p>}
      </div>
      {actions && <div className="sp-page-header__actions">{actions}</div>}
    </header>
  );
}
