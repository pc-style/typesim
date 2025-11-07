import Link from 'next/link';

export function Footer() {
  return (
    <footer className="border-t-4 border-foreground mt-20 py-12 bg-muted">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
          <div>
            <h3 className="font-bold text-lg mb-4">typesim</h3>
            <p className="text-muted-foreground">
              AI-driven realistic typing simulator for Python
            </p>
          </div>
          <div>
            <h3 className="font-bold text-lg mb-4">Links</h3>
            <ul className="space-y-2">
              <li>
                <Link href="/docs" className="text-primary hover:underline">
                  Documentation
                </Link>
              </li>
              <li>
                <a
                  href="https://github.com/pc-style/typesim"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-primary hover:underline"
                >
                  GitHub
                </a>
              </li>
              <li>
                <a
                  href="https://pcstyle.dev"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-primary hover:underline"
                >
                  pcstyle.dev
                </a>
              </li>
            </ul>
          </div>
          <div>
            <h3 className="font-bold text-lg mb-4">License</h3>
            <p className="text-muted-foreground">MIT License</p>
          </div>
        </div>
        <div className="border-t-2 border-foreground pt-8 text-center text-muted-foreground">
          <p>© {new Date().getFullYear()} typesim by pcstyle.dev</p>
        </div>
      </div>
    </footer>
  );
}

