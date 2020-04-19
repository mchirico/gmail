import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Data} from './model/data';

@Injectable({
  providedIn: 'root'
})
export class BackendService {
  public rooturl = 'https://npubsub.cwxstat.io';
  constructor(private  http: HttpClient) {
  }

  getData() {
    return this.http.get<Data[]>(`${this.rooturl}/trainview`);
  }
}
