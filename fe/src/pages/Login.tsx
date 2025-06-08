import { useState } from "react";
import { loginUser } from "../utils/Api";

import styles from "./Login.module.css"
import type { Credentials } from "../models/Credential";
import { useNavigate } from "react-router-dom";
import { HOME_ROUTE } from "../defs/Routes";
import { Button } from "@/components/ui/button";

export default function Login() {
    const [credentials, setCredentials] = useState<Credentials>({
        username: "",
        password: "",
    });
    const [failed, setFailed] = useState(false);

    const navigate = useNavigate()

    const handleSubmit = async (e: any) => {
        e.preventDefault();
        loginUser(credentials).then(({ token }) => {
            localStorage.setItem("token", token);
            localStorage.setItem("username", credentials.username);
            navigate(HOME_ROUTE)
        }).catch((_) => {
            setFailed(true)
        })
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        const updated = { ...credentials, [name]: value };
        setCredentials(updated);
        setFailed(false)
    };


    return (
        <div className="h-[100vh] flex items-center justify-center">
            <div className={`max-w-[400px] mx-auto ${styles.formSection}`}>
                <form onSubmit={handleSubmit} className={styles.form}>
                    <div className={styles.formRow}>
                        <label htmlFor="username">Name:</label>
                        <input
                            type="text"
                            id="username"
                            name="username"
                            value={credentials.username}
                            onChange={handleChange}
                            required />
                    </div>

                    <div className={styles.formRow}>
                        <label htmlFor="password">Password:</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            value={credentials.password}
                            onChange={handleChange}
                            required />
                    </div>
                    {failed && <span className={styles.errorMsg}> Login failed </span>}
                    <Button type="submit">Log in</Button>

                </form>
            </div>
        </div>
    );
}
