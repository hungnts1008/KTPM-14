// PrivateRoute.js
import { Navigate } from 'react-router-dom';
import { isTokenExpired } from '../utils/Auth';
import type { ReactNode } from 'react';
import { LOGIN_ROUTE } from '../defs/Routes';
import NavBar from './NavBar';

type PrivateRouteProps = {
    children: ReactNode;
};

export default function PrivateRoute({ children }: PrivateRouteProps) {
    const token = localStorage.getItem('token');
    if (!token || isTokenExpired(token)) {
        return <Navigate to={LOGIN_ROUTE} replace />;
    }
    return (
        <>
            <NavBar />
            {children}
        </>
    );
}

