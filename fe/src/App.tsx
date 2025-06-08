import './App.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HOME_ROUTE, LOGIN_ROUTE, ROOM_ROUTE } from './defs/Routes';
import Home from './pages/Home';
import Login from './pages/Login';
import NoPage from './pages/NoPage';
import PrivateRoute from './components/PrivateRoute';
import Room from './pages/Room';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path={HOME_ROUTE} element={<PrivateRoute children={<Home />} />} />
                <Route path={ROOM_ROUTE} element={<PrivateRoute children={<Room />} />} />
                <Route path={LOGIN_ROUTE} element={<Login />} />

                <Route path='*' element={<NoPage />} />
            </Routes>
        </BrowserRouter >
    )
}

export default App
