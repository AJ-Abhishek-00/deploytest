import "./globals.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {

  return (
    <html lang="en" suppressHydrationWarning>
      <body className="bg-white dark:bg-gray-900 text-black dark:text-white transition-colors duration-300">
        {children}
      </body>
    </html>
  );

}
