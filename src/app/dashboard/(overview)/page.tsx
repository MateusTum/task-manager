import { roboto } from '@/app/ui/fonts';

export default async function Page() {
    return (
      <main>
        <h1 className={`${roboto.className} mb-4 text-xl md:text-2xl`}>
          Tasks Overview
        </h1>
      </main>
    );
  }