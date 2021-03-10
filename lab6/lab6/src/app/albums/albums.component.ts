import { Component, OnInit } from '@angular/core';
import {Album} from '../album-matrix';
// import {Albums} from '../test-albums';
import {AlbumsService} from '../albums.service';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  ids: number;
  createTitle: string;
  albums: Album[];
  // @ts-ignore
  loading: boolean;
  constructor(private albumsService: AlbumsService)
  {
    this.ids = 101;
    this.createTitle = '';
    this.albums = [];
  }

  ngOnInit(): void {
    this.getAlbums();
  }
  // tslint:disable-next-line:typedef
  getAlbums()
  {
    this.loading = true;
    this.albumsService.getAlbums().subscribe((albums) => this.albums = albums);
    this.loading = false;
  }
  deleteAlbum(id: number): void
  {
    // console.log('delete ' + id);
    this.albums = this.albums.filter((x) => x.id !== id);
    this.albumsService.deleteAlbum(id).subscribe();
  }
  createAlbum(): void
  {
    const temp: Album = {
      id: this.ids,
      title: this.createTitle
    };
    this.createTitle = '';
    this.albums.push(temp);
    this.albumsService.addAlbum(temp);
  }
}
