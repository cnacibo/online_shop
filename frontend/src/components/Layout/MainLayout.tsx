import { ReactNode } from 'react';
import { Header } from '../Header/Header';
import './MainLayout.css';

type Props = {
  children: ReactNode;
};

export const MainLayout = ({ children }: Props) => {
  return (
    <div className="layout">
      <Header />
      <main className="content">{children}</main>
    </div>
  );
};