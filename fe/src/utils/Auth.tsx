import { jwtDecode } from 'jwt-decode';

export function isTokenExpired(token: string) {
    const { exp } = jwtDecode(token);
    if (!exp) {
        return false;
    }
    return Date.now() >= exp * 1000;
}

export function logout() {
    localStorage.removeItem("token")
    localStorage.removeItem("username")
}
