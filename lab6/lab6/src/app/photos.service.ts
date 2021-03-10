import { Injectable } from '@angular/core';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import {Photo} from './photos-matrix';
import {Observable, of} from 'rxjs';
// import {ActivatedRoute} from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class PhotosService {
  constructor(private client: HttpClient) {
  }
  // tslint:disable-next-line:typedef
  getPhotos(id: number): Observable<Photo[]>
  {
    // console.log(this.client.get<Photo[]>(`https://jsonplaceholder.typicode.com/albums/${id}/photos`));
    return this.client.get<Photo[]>(`https://jsonplaceholder.typicode.com/albums/${id}/photos`);
  }
}
