"use client";

export default function SummaryCards() {

  return (

    <div className="grid grid-cols-3 gap-4 mb-6">

      <div className="bg-blue-500 text-white p-4 rounded">
        Total Products: 100
      </div>

      <div className="bg-green-500 text-white p-4 rounded">
        Categories: 5
      </div>

      <div className="bg-purple-500 text-white p-4 rounded">
        Avg Rating: 4.5
      </div>

    </div>

  );

}
