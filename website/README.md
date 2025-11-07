# typesim Website

Modern landing page and documentation site for typesim, built with Next.js 15, TypeScript, Tailwind CSS, and shadcn/ui.

## Features

- **Landing Page** - Modern hero section, features grid, live demo, and how-it-works
- **Documentation** - Comprehensive MDX-based docs with sidebar navigation
- **Neo-Brutal Design** - Sharp corners, thick borders, high contrast with magenta accent
- **Dark Mode** - Full dark mode support with theme toggle
- **Responsive** - Mobile-first design that works on all devices

## Tech Stack

- **Next.js 15** - App Router with React Server Components
- **TypeScript** - Full type safety
- **Tailwind CSS v4** - Utility-first styling
- **shadcn/ui** - Accessible component library
- **MDX** - Markdown with React components
- **next-themes** - Dark mode support

## Getting Started

### Install Dependencies

```bash
npm install
```

### Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to see the site.

### Build for Production

```bash
npm run build
npm start
```

## Project Structure

```
website/
├── app/
│   ├── page.tsx              # Landing page
│   ├── layout.tsx            # Root layout
│   ├── docs/
│   │   ├── page.tsx          # Docs index (redirects)
│   │   └── [...slug]/
│   │       └── page.tsx      # Dynamic docs pages
│   └── globals.css           # Global styles
├── components/
│   ├── ui/                   # shadcn/ui components
│   ├── code-block.tsx        # Syntax-highlighted code
│   ├── terminal.tsx          # Terminal display
│   ├── typing-demo.tsx       # Animated typing demo
│   ├── feature-card.tsx      # Feature card component
│   ├── docs-layout.tsx       # Docs page layout
│   ├── footer.tsx            # Site footer
│   └── theme-provider.tsx    # Theme provider
├── content/
│   └── docs/                 # MDX documentation
│       ├── getting-started.mdx
│       ├── installation.mdx
│       ├── configuration.mdx
│       ├── usage.mdx
│       ├── api.mdx
│       └── examples.mdx
├── lib/
│   └── utils.ts              # Utility functions
├── mdx-components.tsx        # MDX component mapping
├── next.config.ts            # Next.js config
└── package.json
```

## Deployment

### Vercel (Recommended)

1. Push to GitHub
2. Import project in Vercel
3. Deploy automatically

The site is optimized for Vercel deployment with zero configuration needed.

### Other Platforms

The site can be deployed to any platform that supports Next.js:

- Netlify
- Cloudflare Pages
- AWS Amplify
- Railway
- Render

## Customization

### Colors

Edit `app/globals.css` to change the color scheme:

- Primary: `#E6007E` (magenta)
- Background: `#ffffff` / `#000000` (light/dark)
- Foreground: `#000000` / `#ffffff` (light/dark)

### Content

- Landing page: `app/page.tsx`
- Documentation: `content/docs/*.mdx`
- Navigation: `components/docs-layout.tsx`

## License

MIT License - same as typesim
