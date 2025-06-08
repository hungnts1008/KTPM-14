import {
    NavigationMenu,
    NavigationMenuContent,
    NavigationMenuItem,
    NavigationMenuLink,
    NavigationMenuList,
    NavigationMenuTrigger,
} from "@/components/ui/navigation-menu"
import { LOGIN_ROUTE } from "@/defs/Routes";
import { logout } from "@/utils/Auth";
import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
    const username = localStorage.getItem("username");
    const navigate = useNavigate();

    const handleLogout = async () => {
        logout();
        navigate(LOGIN_ROUTE)
    }

    return (
        <NavigationMenu viewport={false} >
            <NavigationMenuList className="w-[100vw] shadow-sm p-[10px] flex justify-between">
                <NavigationMenuItem>
                    <NavigationMenuTrigger>Simple</NavigationMenuTrigger>
                    <NavigationMenuContent>
                        <ul className="grid w-[200px] gap-4">
                            <li>
                                <NavigationMenuLink asChild>
                                    <Link to="#">Components</Link>
                                </NavigationMenuLink>
                                <NavigationMenuLink asChild>
                                    <Link to="#">Documentation</Link>
                                </NavigationMenuLink>
                                <NavigationMenuLink asChild>
                                    <Link to="#">Blocks</Link>
                                </NavigationMenuLink>
                            </li>
                        </ul>
                    </NavigationMenuContent>
                </NavigationMenuItem>
                <NavigationMenuItem>
                    <NavigationMenuTrigger> {username} </NavigationMenuTrigger>
                    <NavigationMenuContent className="right-0">
                        <ul className="grid gap-4">
                            <li>
                                <NavigationMenuLink asChild>
                                    <Link to={LOGIN_ROUTE} className="flex-row items-center gap-2" onClick={handleLogout}>
                                        Log out
                                    </Link>
                                </NavigationMenuLink>
                            </li>
                        </ul>
                    </NavigationMenuContent>
                </NavigationMenuItem>
            </NavigationMenuList>
        </NavigationMenu>
    )
}
