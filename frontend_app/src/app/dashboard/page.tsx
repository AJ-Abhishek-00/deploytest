"use client";

import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import SummaryCards from "@/components/SummaryCards";
import ProductTable from "@/features/products/components/ProductTable";

export default function Dashboard() {

  return (
<div className="bg-white dark:bg-gray-900 text-black dark:text-white min-h-screen">


      <Navbar />

      <div className="flex">

        <Sidebar />

        <div className="p-6 w-full">

          <SummaryCards />

          <ProductTable />

        </div>

      </div>

    </div>

  );

}
