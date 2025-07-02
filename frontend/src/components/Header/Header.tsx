import './Header.css';
import { Link } from 'react-router-dom';

export const Header = () => {
  return (
    <header className="header">
        <nav className="nav">
            <Link to="/">Home</Link>
            <Link to="/orders">Orders</Link>
            <Link to="/account">Account</Link>
        </nav>
        <h1 className="title">Online Shop</h1>
        <div className="right-spacer" />
    </header>
  );
};