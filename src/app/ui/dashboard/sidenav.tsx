"use client";

import Link from 'next/link';
import HomeLogo from '@/app/ui/home-logo';
import NavLinks from '@/app/ui/dashboard/nav-links';
import { usePathname } from "next/navigation";
import clsx from "clsx";

export default function SideNav() {
    const pathname = usePathname();
    const dashboardPath = "/dashboard";

    return (
    <div className="flex h-full flex-col px-3 py-4 md:px-2">
        <Link
            className={clsx(
                "mb-2 flex h-20 items-end justify-start rounded-md bg-primary hover:bg-secondary p-4 md:h-20",
                {
                    "bg-tertiary text-white hover:bg-tertiary": pathname === dashboardPath,
                }
                )}
            href="/dashboard"
        >
        <div className="flex justify-center items-center w-full md:w-full">
            <HomeLogo />
        </div>
        </Link>
        <div className="flex grow flex-row justify-start space-x-2 md:flex-col md:space-x-0 md:space-y-2">
            <NavLinks />
        </div>
    </div>
    );
}