import { roboto } from '@/app/ui/fonts';
import TasksTable from '@/app/ui/tasks/table';

export default async function Page() {
    return (
      <main>
        <h1 className={`${roboto.className} mb-4 text-xl md:text-2xl`}>
          Tasks
        </h1>
        <TasksTable />
      </main>
    );
  }