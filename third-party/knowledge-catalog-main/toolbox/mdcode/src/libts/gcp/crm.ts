// API client for Cloud Resource Manager
//

import * as api from './api';
import * as context from './context';


export interface Project {
  name: string;
  projectId: string;
  [key: string]: any;
}


const PROJECT_NUM_TO_ID_CACHE = new Map<string, string>();
PROJECT_NUM_TO_ID_CACHE.set('655216118709', 'dataplex-types');


export class ResourceManagerClient extends api.ApiClient {

  constructor(ctx: context.ApiContext) {
    super('https://cloudresourcemanager.googleapis.com', 'v3', ctx);
  }

  async getProject(project: string): Promise<api.ApiResult<Project>> {
    const name = `projects/${project}`;
    return await this._get(name);
  }
}

export async function fixProject(resource: string, ctx: context.ApiContext): Promise<string> {
  // projects/<project_id> or projects/<project_number> -> projects/<project_id>

  const parts = resource.split('/');
  if (/^\d+$/.test(parts[1])) {
    let id = PROJECT_NUM_TO_ID_CACHE.get(parts[1]);
    if (!id) {
      const res = await new ResourceManagerClient(ctx).getProject(parts[1]);
      id = res.status == 200 ? res.result?.projectId : '';
    }

    if (id) {
      PROJECT_NUM_TO_ID_CACHE.set(parts[1], id);
      parts[1] = id;
    }
    resource = parts.join('/');
  }

  return resource;
}
