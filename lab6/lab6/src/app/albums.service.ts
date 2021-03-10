import { Injectable } from '@angular/core';
// import {Albums} from './test-albums';
import {Album} from './album-matrix';
import {Observable, of} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Photo} from './photos-matrix';

@Injectable({
  providedIn: 'root'
})
export class AlbumsService {
  option = new HttpHeaders({'Content-Type': 'application/json'});
  BASIC_URL: string;
  constructor(private client: HttpClient) {
    this.BASIC_URL = 'https://jsonplaceholder.typicode.com';
  }
  // tslint:disable-next-line:typedef
  getAlbums(): Observable<Album[]>
  {
    return this.client.get<Album[]>(`${this.BASIC_URL}/albums`);
    // return of(Albums);
  }
  // tslint:disable-next-line:typedef
  getAlbum(id: number): Observable<Album>
  {
    return this.client.get<Album>(`${this.BASIC_URL}/albums/${id}`);
    // const album = Albums.find((x) => x.id === id);
    // // @ts-ignore
    // return of(album);
  }
  addAlbum(album: Album): Observable<Album>
  {
    // @ts-ignore
    return this.client.post<Album>(`${this.BASIC_URL}/albums`, album, this.option);
  }
  updateAlbum(album: Album): Observable<Album>
  {
    // @ts-ignore
    return this.client.put<Album>(`${this.BASIC_URL}/albums/${album.id}`, album, this.option);
  }
  deleteAlbum(id: number): Observable<any>
  {
    return this.client.delete(`${this.BASIC_URL}/albums/${id}`);
  }
}
